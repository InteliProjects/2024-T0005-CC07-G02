import { MetadataRoute } from 'next'
 
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'vivo',
    short_name: 'vivo',
    description: 'Next.js App',
    start_url: '/dashboard',
    display_override: ["standalone", "fullscreen", "minimal-ui"],
    display: 'standalone',
    theme_color: '#fff',
    icons: [
      {
        src: '/favicon.ico',
        sizes: 'any',
        type: 'image/x-icon',
      },
    ],
  }
}