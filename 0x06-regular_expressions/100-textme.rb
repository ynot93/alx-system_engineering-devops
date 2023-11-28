#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: ./100-textme.rb <log_entry>"
  exit(1)
end

log_entry = ARGV[0]
sender = log_entry[/\[from:(.*?)\]/, 1]
receiver = log_entry[/\[to:(.*?)\]/, 1]
flags = log_entry[/\[flags:(.*?)\]/, 1]

puts "#{sender},#{receiver},#{flags}"
