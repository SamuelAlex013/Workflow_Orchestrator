import { ImageResponse } from 'next/og'

export const runtime = 'edge'
export const size = {
    width: 32,
    height: 32,
}
export const contentType = 'image/png'

export default function Icon() {
    return new ImageResponse(
        (
            <div
                style={{
                    background: 'linear-gradient(135deg, #38BDF8 0%, #6366F1 100%)',
                    width: '100%',
                    height: '100%',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    borderRadius: '20%',
                }}
            >
                <svg
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    {/* Gear shape */}
                    <path
                        d="M12 2L13.5 5.5L17 6L14.5 9L15 12.5L12 11L9 12.5L9.5 9L7 6L10.5 5.5L12 2Z"
                        fill="white"
                        opacity="0.9"
                    />
                    {/* Center circle */}
                    <circle cx="12" cy="8.5" r="2.5" fill="#6366F1" />
                    {/* Automation arrows */}
                    <path
                        d="M8 14L12 17L16 14"
                        stroke="white"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        opacity="0.9"
                    />
                    <path
                        d="M12 17V20"
                        stroke="white"
                        strokeWidth="2"
                        strokeLinecap="round"
                        opacity="0.9"
                    />
                    {/* Small dots for workflow */}
                    <circle cx="5" cy="12" r="1.5" fill="white" opacity="0.7" />
                    <circle cx="19" cy="12" r="1.5" fill="white" opacity="0.7" />
                </svg>
            </div>
        ),
        {
            ...size,
        }
    )
}
