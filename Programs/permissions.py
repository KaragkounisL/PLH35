# Functions that calculates the permissions of a file or directory with the umask

def calc_files(umask):
    """
    Calculates the permissions of a file with the umask
    """
    not_umask = ~umask
    # Default value for files:  666
    # Calculate the permissions of the file
    permissions = 0o666 & not_umask
    # Print the permissions
    return oct(permissions)


def calc_directories(umask):
    """
    Calculates the permissions of a directory with the umask
    """
    not_umask = ~umask
    # Default value for directories:  777
    # Calculate the permissions of the directory
    permissions = 0o777 & not_umask
    # Print the permissions
    return oct(permissions)


# Convert the permissions to rwxrwxrwx format
def calc_rwx(permissions):
    """
    Calculates the rwxrwxrwx permissions
    """
    # Convert the permissions to rwxrwxrwx format
    rwx = permissions[2:].replace("0", "---").replace("1", "--x").replace("2", "-w-").replace(
        "3", "-wx").replace("4", "r--").replace("5", "r-x").replace("6", "rw-").replace("7", "rwx")
    # Return the rwxrwxrwx permissions
    return rwx


# Notes: Remember that s is the setuid bit and what it does is that it makes the file executable with the permissions of the owner of the file.
#        The setgid bit is similar to the setuid bit, but it makes the file executable with the permissions of the group of the file (also s).
#        The sticky bit is put at the end of the permissions, represented by a “t” in the rwxrwxrwx format, set with the octal 1000 and it limits the permissions of the file to the owner of the file.
#        d is the directory bit (attribute not permission) and is at the start of the permission format.
# Permission commands in Unix:
# chmod - change the permissions of a file
# chown - change the owner of a file
# chgrp - change the group of a file
# umask - modifies the creation permissions of newly created files and directories


def umask_print(umask):
    print("#--- Files ---#")
    print("Octal:", calc_files(umask)[2:])
    print("Format rwx:", calc_rwx(calc_files(umask)))
    print("#--- Directories ---#")
    print("Octal:", calc_directories(umask)[2:])
    print("Format rwx:", calc_rwx(calc_directories(umask)))


umask = 0o123
umask_print(umask)

permissions = oct(0o656)
print("Formating for given permissions",
      permissions[2:], ": ", calc_rwx(permissions))
