## Verified Commit Setup Summary
- GitHub Username: akhileshwarreddy1706
- Verified Email: abommineni2024@fau.edu
- GPG Key ID: BE816EA725A81293
- Commit Signing: Enabled Globally
- GPG_TTY: Persistent via ~/.zshrc
- Verified Commit Example: https://github.com/akhileshwarreddy1706/Image2Image-Text2Image-video-generation-for-FAU-Engineering/commits/main

### Transfering Verified Setup to Another System
To reuse your verified identity on another laptop:

1. Export your private GPG key:
   gpg --export-secret-keys --armor BE816EA725A81293 > my-gpg-private-key.asc

2. Copy the exported file safely (e.g., encrypted USB, or AirDrop securely).

3. On the new system, import it:
   gpg --import my-gpg-private-key.asc

4. Configure Git again:
   git config --global user.name 'akhileshwarreddy1706'
   git config --global user.email 'abommineni2024@fau.edu'
   git config --global user.signingkey BE816EA725A81293
   git config --global commit.gpgsign true
   echo 'export GPG_TTY=/dev/ttys000' >> ~/.zshrc

Then test with a signed commit:
   git commit -S -m 'Verified commit test'

