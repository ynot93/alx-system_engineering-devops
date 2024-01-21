# Turn off password authentication
augeas { 'Turn off passwd auth':
  context => '/etc/ssh/ssh_config',
  changes => [
    'set PasswordAuthentication no',
  ],
}

# Specify private key file
augeas { 'Declare identity file':
  context => '/etc/ssh/ssh_config',
  changes => [
    'set IdentityFile ~/.ssh/school',
  ],
}
