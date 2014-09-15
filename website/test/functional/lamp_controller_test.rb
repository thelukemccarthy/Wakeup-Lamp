require 'test_helper'

class LampControllerTest < ActionController::TestCase
  test "should get lamp" do
    get :lamp
    assert_response :success
  end

end
