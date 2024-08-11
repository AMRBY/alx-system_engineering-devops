# PUPPET manifest to create a file with content and permissions

file { '/tmp/school':
ensure  => present,
owner   => www-data,
group   => www-data,
mode    => '0744',
content => 'I love Puppet',
}
