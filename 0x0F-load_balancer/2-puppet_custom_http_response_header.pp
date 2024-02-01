# Create custom HTTP header response with Puppet

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Define custom header configuration
$custom_header_config = "server_name _;\n\t add_header X-Served-By $hostname;"

# Configure Nginx with custom HTTP header
file { 'etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "
    $custom_header_config
  ",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}
