Q1. Introduction to Vulnerabilities and OWASP Top 10

Step 1: Start Juice Shop

docker start juice-shop 2>/dev/null || docker run -d --name juice-shop -p 3000:3000 bkimminich/juice-shop
firefox http://localhost:3000

Step 2: Open the Score Board

In Juice Shop, open the hidden score board. This shows solved vulnerabilities and is useful for screenshots.

http://localhost:3000/#/score-board

Step 3: Identify SQL Injection in login

Go to Account > Login. Try this only in Juice Shop.

Email: ' OR 1=1--
Password: anything

Step 4: Identify XSS in search

Use the Juice Shop search box. If the alert appears, XSS is confirmed.

<iframe src="javascript:alert(`xss`)">


Q2. Network Scanning and Reconnaissance

Step 1: Collect local network information

ip addr show
ifconfig
arp -a
route -n

Step 2: Ping safe targets

ping -c 4 localhost
ping -c 4 google.com

Step 3: Scan local Juice Shop service

docker start juice-shop
nmap -sV -p 3000 localhost

Step 4: Scan a safe VM target if provided

Replace TARGET_IP with your own Metasploitable2 or instructor-provided IP.

TARGET_IP=192.168.56.101
ping -c 4 $TARGET_IP
nmap -sV $TARGET_IP
nmap -A -oN ~/EH_Practicals/recon_scan.txt $TARGET_IP


Q3. Network Traffic Analysis using Wireshark

Step 1: Open a sample pcap

wireshark ~/EH_Practicals/pcaps/http.cap

Step 2: Understand the Wireshark windows

Observe the three main panes: packet list at top, packet details in middle, packet bytes at bottom.

Step 3: Click a packet and expand layers

Expand Frame, Ethernet, IP, TCP, and HTTP. Write one line for each layer in your observation.

Step 4: Follow TCP stream

Right-click an HTTP packet > Follow > TCP Stream. This reconstructs the request and response. Take a screenshot.

Step 5: Save observations

Write source IP, destination IP, protocol, source port, destination port, and one HTTP method you observed.


Q4. SQL Injection on OWASP Juice Shop

Step 1: Start Juice Shop and open login

docker start juice-shop
firefox http://localhost:3000
# In the web page: Account > Login

Step 2: Test normal login failure

Enter any fake email/password first. This shows normal behaviour before injection.

Step 3: Perform login bypass SQL Injection

Enter this payload in the Email field and any text in the password field:

' OR 1=1--

Step 4: Record extracted/visible sample data

After login, open the account/profile menu and record what account identity is visible. Also open the Score Board and record the solved Login Admin challenge if it appears.

Step 5: Explain the query logic

Original idea:

SELECT * FROM Users WHERE email = '<email>' AND password = '<password>';

Injected idea:

SELECT * FROM Users WHERE email = '' OR 1=1--' AND password = 'anything';

OR 1=1 is always true, and -- comments out the rest of the query.


Q5. Alternate Data Streams (ADS) in Windows

Step 1: Create a lab folder in Command Prompt

cd %USERPROFILE%\Desktop
mkdir ads_lab
cd ads_lab

Step 2: Create a visible file

echo This is a visible file > visible.txt
type visible.txt

Step 3: Create an alternate data stream

echo This is hidden ADS data > visible.txt:secret.txt

Step 4: Show that normal directory listing does not reveal it

dir
type visible.txt

Step 5: Read the hidden stream

more < visible.txt:secret.txt

Step 6: Detect ADS using dir /R

dir /R

Step 7: Detect ADS using PowerShell

PowerShell
Get-Item -Path .\visible.txt -Stream *
exit

Step 8: Clean up

del visible.txt
cd ..
rmdir ads_lab


Q6. Password Cracking using John the Ripper

Step 1: Create SHA-256 sample hashes

mkdir -p ~/EH_Practicals/john
cd ~/EH_Practicals/john
cat > hashes_sha256.txt << 'EOF_HASHES'
user1:ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
user2:65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5
user3:1c8bfe8f801d79745c4631d09fff36c82aa37fc4cce4fc946683d7b336b63032
EOF_HASHES
# These correspond to password123, qwerty, and letmein.

Step 2: Run John with rockyou

sudo gunzip /usr/share/wordlists/rockyou.txt.gz 2>/dev/null || true
john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt hashes_sha256.txt
john --show --format=raw-sha256 hashes_sha256.txt

Step 3: Optional incremental mode

This can run for a long time. Stop with Ctrl+C when needed.

john --format=raw-sha256 --incremental hashes_sha256.txt


Q7. Vulnerability Assessment using OpenVAS/Nessus

Step 1: Make the target reachable

Start Juice Shop in Kali and find the Kali VM IP. From macOS, verify that http://KALI_IP:3000 opens. If it does not open, use VMware NAT/host-only settings.

# In Kali:
docker start juice-shop
ip -4 addr show

Step 2: Open Nessus on the host

https://localhost:8834

Step 3: Create a basic scan

In Nessus: New Scan > Basic Network Scan. Name it EH-7 Vulnerability Assessment. Target should be the Kali VM IP or instructor-provided test VM IP, not a public IP.

Step 4: Launch and wait

The scan may take 10-30 minutes. Do not run aggressive scans on networks not owned.

Step 5: Review findings

Open the scan results. Note severity, plugin name, affected host, port, description, and recommendation.

Step 6: Export report

Click Export and choose PDF or HTML if available.


Q8. Reconnaissance on Metasploitable2 Machine

Step 1: Start the target safely

Boot Metasploitable2 only on NAT/host-only/private networking. Do not use bridged/public networking for this VM.

Step 2: Find the target IP

Inside Metasploitable2, run ifconfig or ip addr. If using another target, write down the provided IP.

Step 3: Ping from Kali

TARGET_IP=192.168.56.101
ping -c 4 $TARGET_IP

Step 4: Run Nmap discovery and service scans

nmap -sV $TARGET_IP
sudo nmap -O $TARGET_IP
sudo nmap -A -oN ~/EH_Practicals/metasploitable2_recon.txt $TARGET_IP
cat ~/EH_Practicals/metasploitable2_recon.txt

Step 5: Prepare an observation table

Record port, protocol, service, version, and security remark. Do not exploit anything.


Q9. Packet Filtering and Protocol Analysis

Step 1: Open HTTP pcap

wireshark ~/EH_Practicals/pcaps/http.cap

Step 2: Apply HTTP filters

Type each filter in the display filter bar and press Enter.

http
http.request
tcp.port == 80
http.request.method == "GET"

Step 3: Open DNS pcap

wireshark ~/EH_Practicals/pcaps/dns.cap

Step 4: Apply DNS filters

dns
dns.qry.name
dns.flags.response == 0
dns.flags.response == 1

Step 5: Apply TCP filters

Use either pcap file.

tcp
tcp.flags.syn == 1
tcp.flags.ack == 1
tcp.analysis.retransmission

Step 6: Use statistics menu

In Wireshark, open Statistics > Protocol Hierarchy and Statistics > Conversations.


Q10. Ethical Hacking Lab Environment Setup

Step 1: Document host and VM specs

Write device model, RAM, free storage, Kali VM CPU, Kali VM RAM, disk size, and network mode.

Step 2: Show Kali is installed

whoami
hostnamectl
ip addr show

Step 3: Show required tools are installed

nmap --version
wireshark --version
john --list=build-info | head
docker --version
python3 --version

Step 4: Show Juice Shop is running

docker ps
docker start juice-shop
firefox http://localhost:3000

Step 5: Show vulnerable target plan

If you have Metasploitable2, screenshot it booted and its IP.

Step 6: Take a clean snapshot

In VMware Fusion, choose Snapshots > Take Snapshot. Name it Clean Kali Lab. This lets recover if something breaks.
