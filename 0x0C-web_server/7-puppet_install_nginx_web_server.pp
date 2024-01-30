# Install a nginx web server with Puppet
# Install nginx
package { 'nginx':
  ensure => installed,
}

# Configure redirect
file_line { 'redirect':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default server',
  line   => 'rewrite ^redirect_me https://www.github.com/tony93/ permanent',
}

# Enable the 301 page
file { '/etc/nginx/sites-available/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File_line['redirect'],
}

# Create the Hello World page
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package ['nginx'],
}

# Restart nginx server
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
  require   => Package['nginx']
}
