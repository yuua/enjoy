# coding:utf-8  

require 'yaml'

a = YAML.load_file('image.yml')

p a['img'].sample
