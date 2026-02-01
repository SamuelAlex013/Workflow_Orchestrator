# TsharkNode – Custom n8n Node for Network Scanning

TsharkNode is an n8n community node.

TsharkNode is a custom n8n node designed to scan networks using Tshark.  
[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

## Key Features

- **Trigger New Frames (Probe/Beacon):** Automatically trigger the workflow when new frames is detected.
- **Channel Hopping:** Cycle through specified channels to capture wireless traffic from multiple frequencies.
- **Advanced Parsing:** Extract key fields such as frame type, MAC address, SSID, frequency, and signal strength.

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

Install with:

```bash
npm i n8n-nodes-tshark
```

## Dependencies:
- **Tshark:** Ensure that Tshark is installed on your n8n instance.
- **Monitor Mode Interface:** A compatible network interface capable of operating in monitor mode is required to capture wireless traffic. Make sure your WiFi adapter supports monitor mode and is properly configured (e.g., using `iw` or `airmon-ng`).

For example, on Debian/Ubuntu: 
```bash
sudo apt-get install tshark

ip link set wlan1 down 
iw dev wlan1 set type monitor
ip link set wlan1 up
```

## Disclaimer
The TsharkNode for n8n is intended for authorized security assessments and internal network audits only. Unauthorized scanning of networks, systems, or devices without explicit permission may violate laws and regulations.

By using this node, you acknowledge that:
*	You have explicit authorization to scan the target network.
*	You assume full responsibility for any consequences arising from its use.
*	The developers and contributors of this node are not liable for any misuse or damages caused.

⚠ Always obtain proper authorization before conducting any network scan. ⚠

## Compatibility

Developed using n8n version 1.64

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Tshark Documentation](https://www.wireshark.org/docs/man-pages/tshark.html)

