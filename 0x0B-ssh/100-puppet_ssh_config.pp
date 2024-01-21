# Turn off password authentication and
# specify private key file to use

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
    Host *
      IdentifyFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
