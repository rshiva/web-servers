require 'rubygems'
require 'sinatra'


class ExampleApp < Sinatra::Base
  get '/' do
    erb :index
  end

  get '/hi' do
  "Hello World! :)"
end
end

# get '/' do
#   "Hello and Goodbye"
# end

# get '/hi' do
#   "Hello World! :)"
# end

# get '/bye' do
#   "Goodbye World! :("
# end