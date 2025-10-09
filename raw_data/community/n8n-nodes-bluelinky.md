# n8n-bluelinky

n8n community node that wraps the `bluelinky` npm package to control Hyundai / Kia / Genesis vehicles from n8n.

Features:
- List vehicles on your account
- Get vehicle status
- Get vehicle location
- Lock / Unlock
- Start / Stop engine or climate

## Install

Enable Community Nodes in n8n and install this package:

- From n8n UI: Settings → Community Nodes → Install → enter `n8n-nodes-bluelinky`
- Or with npm in your n8n deployment:
  - npm install n8n-nodes-bluelinky

## Credentials

Create “BlueLinky API” credentials with:
- Username (email)
- Password
- Region (EU/US/CA)
- Brand (Hyundai/Kia/Genesis)
- Language (default: en)
- PIN (if required by your region for lock/unlock/start actions)

## Node usage

The node exposes the following operations:

- List Vehicles — returns VIN and basic info
- Get Vehicle Status — optionally refreshes and returns parsed status
- Get Location — returns current coordinates if available
- Lock / Unlock — remote door lock/unlock
- Start Engine/Climate — includes options: Air Control, Defrost, Heating Temperature, Duration
- Stop Engine/Climate — stops a previous start command

Vehicle selection:
- Provide VIN to target a specific vehicle, or
- Use Vehicle Index (0-based) when VIN is not set (defaults to 0)

## Notes

- Availability of features depends on your vehicle, brand, region, and BlueLink service.
- Some actions may require a PIN in certain regions.
- This project is not affiliated with Hyundai/Kia/Genesis.

## Development

- Build: `npm run build`
- Watch: `npm run watch`

## License

MIT
