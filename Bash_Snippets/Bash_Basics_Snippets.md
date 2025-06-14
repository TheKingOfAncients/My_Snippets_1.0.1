## Basic File Management

ls: [Insert description here]

cd: [Insert description here]
#### .. : Goes back one level; can be combinded with /
#### ~: Goes back to the home directory.


## File Operations

cp: [Insert description here]

cp -r [Insert file to be copied] [Insert name of soon to be copied filed]

mv: [Insert description here]

rm: [Insert description here]

rm [Insert folder to be deleted]

cat: Views a file's contents

cat [Insert file to be viewed]

touch: Create a new file.

touch [Insert name of file to be created]


nano: Opens the text editor "nano"

grep: Allows one to preform text searches in a file.

grep "[Insert text to be searched for]" [Insert file to be search]


## File Permissions

chmod: Allows one to change the premissions of a file (who can do what to it)
#### =x [Insert script name here] Allows a newly created file to be excutable. 

./[Insert name of script]
#### Allows one to run/excuete a script


## Text Manipulation

echo: Allows one to display text.

echo "[Insert text between these two double quotes for them to be displayed.]"

## Compression

tar: a Shell Command for combining multiple computer files into a single archive file. 


### Snippets
tar -cvf [Insert desired name of archive here] [Insert location(s) 
of files and/or folders to be combined]

# -cvf
#### Creates the archive, lists processes out in details, and allows it to be named / specify, respectively

# -xvf
#### Extracts the contents of the archives, then listed, and specify the file.

#### tar -czf [filename]_$(date +%Y%m%d_%H%M%S).tar.gz [Insert location(s) 
of files and/or folders to be combined]
###### Allows one to create a tar file w/ a timestamp.


## Encryption

gpg: (aka GNU Privacy Guard; GnuPG), a software program that is used for 
many types of encryption including symmeetric-keyu cryptography and public-key cryptography.

### Snippets

gpg -c [Insert filename here to be encrypted.)
#### Note: The writer will be prompted for a password/passphrase.

gpg -o [Insert desired future name of the soon to be decrypted file] -d [Insert encrypted filename here]


openssl: a command line tool used for various cryptographic operations, including:
#### Generating keys
#### Creating certificates
#### Managing SSL/TLS


#### Snippets

pkg install openssl-tool 
#### Note: For installing openssl

openssl enc -aes-256-cbc -salt -in [Insert filename here to be encrypted.] -out [Insert desired future name of the soon to be decrypted file].enc
#### To Encrypt a file.
#### Note: -aes256-cbc is the encryption algorithm; -salt adds randomness to one's password. 


openssl enc -aes-256-cbc -d -in [Insert filename here to be deencrypted.].enc - out [Insert desired future name of the soon to be decrypted file]


## Encryption:Checksums

sha256sum [Insert file to be assigned a unique code that depends completely on its digital makeup]




## Synchronation

rclone: [Insert description here]

rclone copy [Insert files/folders to be copied/duplicated in the form of a path] [Insert name of remote  directory}:[Insert name of directory to recieved these new files]

rclone copy /data remote:example --progress --bwlimit 1M
#### --progress: Shows real-time progress --bwlimit: Limits bandwidth (in this case to 1 MB)

rclone copy /source remote:example --update
#### --update: Skips files that are newer at the destination. 

Other rclone flags:
#### --dry-run: Shows what would be copied without actually doing it
#### --verbose: Increase output verbosity
#### --exclude "*.tmp": Exclude temporary files
