class LampController < ApplicationController
  def lamp
    
  end
  
  def update
    if params[:commit] == 'Off'
      @lamp_state = 'Off'
    elsif params[:commit] == 'Low'
      @lamp_state = 'Low'
    elsif params[:commit] == 'Medium'
      @lamp_state = 'Medium'
    elsif params[:commit] == 'High'
      @lamp_state = 'Heigh'
    end
    redirect_to "/"
  end
end
