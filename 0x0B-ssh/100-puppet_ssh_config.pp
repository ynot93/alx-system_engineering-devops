# Turn off password authentication
augeas { 'Turn off passwd auth':
  context => '~/.ssh/config',
  changes => [
    'set PasswordAuthentication no',
  ],
}

# Specify private key file
augeas { 'Declare identity file':
  context => '~/.ssh/config',
  changes => [
    'set IdentityFile ~/.ssh/school',
  ],
}
