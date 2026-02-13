"use client"

import { useState } from "react"
import { Play } from "lucide-react"

export function Demo() {
  const [playing, setPlaying] = useState(false)

  return (
    <section id="demo" className="py-16 md:py-24">
      <div className="mx-auto max-w-4xl px-6">
        <div className="mx-auto max-w-2xl text-center">
          <p className="text-sm font-semibold uppercase tracking-widest text-primary">
            Demo
          </p>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight text-foreground md:text-4xl">
            See SafeSight in action
          </h2>
          <p className="mt-4 text-pretty leading-relaxed text-muted-foreground">
            Watch a 30-second walkthrough of how detection, verification, and
            response work together seamlessly.
          </p>
        </div>

        <div className="relative mt-10 overflow-hidden rounded-2xl border border-border bg-foreground/5 shadow-lg">
          {!playing ? (
            <button
              onClick={() => setPlaying(true)}
              className="group relative flex aspect-video w-full items-center justify-center focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
              aria-label="Play demo video"
              suppressHydrationWarning
            >
              {/* Thumbnail placeholder */}
              <div className="absolute inset-0 bg-gradient-to-br from-primary/10 to-primary/5" />
              <div className="absolute inset-0 flex flex-col items-center justify-center gap-4">
                <div className="flex h-16 w-16 items-center justify-center rounded-full bg-primary shadow-lg transition-transform group-hover:scale-110">
                  <Play className="h-7 w-7 fill-primary-foreground text-primary-foreground" />
                </div>
                <span className="text-sm font-medium text-foreground">
                  Click to play demo
                </span>
              </div>
              {/* Simulated thumbnail content */}
              <div className="flex aspect-video w-full items-center justify-center">
                <div className="grid grid-cols-3 gap-3 opacity-20">
                  {Array.from({ length: 6 }).map((_, i) => (
                    <div key={i} className="h-16 w-24 rounded-lg bg-foreground/30" />
                  ))}
                </div>
              </div>
            </button>
          ) : (
            <div className="flex aspect-video w-full items-center justify-center bg-foreground/5">
              <div className="text-center">
                <div className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-primary/10">
                  <Play className="h-7 w-7 text-primary" />
                </div>
                <p className="text-sm font-medium text-foreground">
                  Demo video playing
                </p>
                <p className="mt-1 text-xs text-muted-foreground">
                  Replace this with your MP4 walkthrough video
                </p>
              </div>
            </div>
          )}
        </div>

        <p className="mt-4 text-center text-xs text-muted-foreground">
          Captions and transcript available. All footage is simulated for
          demonstration purposes.
        </p>
      </div>
    </section>
  )
}
