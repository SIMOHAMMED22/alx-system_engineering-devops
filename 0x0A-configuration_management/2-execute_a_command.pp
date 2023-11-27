# This Puppet manifest kills a process named killmenow
exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
  subscribe   => File['/path/to/your/actual/file'],
  logoutput   => true,
  unless      => 'pgrep killmenow',
}
