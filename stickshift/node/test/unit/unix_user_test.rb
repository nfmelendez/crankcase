#!/usr/bin/ruby
#--
# Copyright 2012 Red Hat, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#++
#
# Test the StickShift unix_user model
#
require 'stickshift-node/model/unix_user'
require 'test/unit'

# Run unit test manually
# ruby -Istickshift/node/lib/:stickshift/common/lib/ stickshift/node/test/unit/unix_user_test.rb 
class TestUnixUserModel < Test::Unit::TestCase

  def assert_file_exists?(file)
    assert File.exists?(file), "#{file} not found"
  end

  def test_initialize
    gear_uuid = Process.euid.to_s
    user_uid = Process.euid.to_s
    app_name = 'UnixUserTestCase'
    namespace = 'jwh201204301647'

    FileUtils.rm_rf("/tmp/homedir")
    o = StickShift::UnixUser.new(gear_uuid, gear_uuid, user_uid, app_name, namespace)
    assert_not_nil o

    o.initialize_homedir("/tmp/", "/tmp/homedir/", "stickshift/abstract/")
    assert_file_exists?("/tmp/homedir")
    assert_file_exists?("/tmp/homedir/app")
    assert_file_exists?("/tmp/homedir/app/.state")
    assert_equal(Process.euid, File.stat("/tmp/homedir/app/.state").uid)
    assert_file_exists?("/tmp/homedir/.tmp")
    assert_file_exists?("/tmp/homedir/.env")
    assert_file_exists?("/tmp/.httpd.d")
    assert_file_exists?("/tmp/.httpd.d/#{gear_uuid}_#{namespace}_#{app_name}")
  end
end

