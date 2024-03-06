# Puppet manifest to install and configure Nginx with a 301 redirect

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx site
file_line { 'redirect_config':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/millyanne93 permanent;',
}

# Enable the Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File_line['redirect_config'],
}

# Create index.html with "Hello World!"
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
  require   => Package['nginx'],
}
