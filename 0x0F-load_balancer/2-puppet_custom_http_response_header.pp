# Create custom HTTP header response with Puppet

# Install Nginx package
package { 'nginx':
  ensure  => 'installed',
}

# Create an index page
file { 'var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
}

# Define custom header configuration
$custom_header_config = "server_name _;\n\tadd_header X-Served-By $hostname;"

# Create custom 404 page
file { '/var/www/html/custom404.html':
  content => "Ceci n'est pas une page\n",
  ensure  => present,
}

# Configure Nginx with custom HTTP header and 404 page
file { 'etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "
    $custom_header_config
    error_page 404 /custom404.html;
    location = /custom404.html {
      root var/www/html;
      internal;
    }
  ",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
}
