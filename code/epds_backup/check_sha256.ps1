$log_file_path = "D:\log\info_" + (Get-Date -Format "yyyy-MM-dd") + ".log"
$error_log_file = "D:\log\error_" + (Get-Date -Format "yyyy-MM-dd") + ".log"


$tar_dir_list = @("D:\DailyBackup\KIS_JD", "D:\DailyBackup\KIS_YP")
$interface_alias = "Ethernet0"


function write_log_file($message) {
    (Get-Date).ToString() + " - " + $message  >> $log_file_path
}
function write_error_log($message) {
    (Get-Date).ToString() + " - " + $message  >> $error_log_file
}


function get_file_list($dir_path, $exclude_extension = '.sha256') {
    write_log_file("begin check files under ${dir_path}")
    $result = @()
    $file_list = (Get-ChildItem $dir_path |  ? { $_.PsIsContainer -eq $false })
    Foreach ($file_item in $file_list) {
        if ($file_item.Extension -ne $exclude_extension) {
            $result += @($file_item)
        }
    }
    return $result
}

function cacl_sha256($file_list) {
    Foreach ($file_item in $file_list) {
        $full_name = $file_item.FullName
        $sha_file = ( -Join ( $full_name, ".sha256"))
        $expect_sha = ( -Join ((CertUtil  -hashfile $full_name sha256)[1], ", ", $file_item.Name))
        $host_info_array = @(
            (hostname).ToString(),
            ((Get-NetIPAddress -AddressFamily IPV4 -InterfaceAlias $interface_alias).IPAddress).ToString(),
            (Get-Date -Format "yyyy-MM-dd_HH:mm:ss")
        )


 
        if (Test-Path $sha_file) {
            
            if ($expect_sha -ne (Get-Content $sha_file)[0]) {                
                write_error_log(( -Join ( "file: ${full_name}", [Environment]::NewLine, "expect value: ${expect_sha}", [Environment]::NewLine, "actual value: " + (Get-Content $sha_file))))
                write_log_file("File ${sha_file} Exist but Not Match")
            }
            else {
                write_log_file("File ${sha_file} Exist and Match")
                return
            }
            
            if (-Not (Get-Content $sha_file | findstr (hostname)).contains((hostname) + ",")) {
                $host_info_array -Join ", ">>  $sha_file
            }
        }
        else {
            $final_rst = @($expect_sha, ($host_info_array -Join ", "))
            $final_rst -join [Environment]::NewLine > $sha_file
            
        }
       
    }
}


foreach ($tar_dir in $tar_dir_list) {
    
    $file_list = get_file_list($tar_dir)

    cacl_sha256($file_list)
}