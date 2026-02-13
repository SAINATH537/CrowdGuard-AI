import Image from "next/image"
import { Play, ShieldCheck, Clock, Lock } from "lucide-react"

export function Hero() {
  return (
    <section className="relative overflow-hidden pb-16 pt-16 md:pb-24 md:pt-24">
      <div className="mx-auto flex max-w-6xl flex-col items-center gap-12 px-6 lg:flex-row lg:gap-16">
        {/* Copy */}
        <div className="flex max-w-xl flex-col items-center text-center lg:items-start lg:text-left">
          <h1 className="text-balance text-4xl font-bold leading-tight tracking-tight text-foreground md:text-5xl lg:text-[3.25rem]">
            Detect fights. Verify fast. Protect your community.
          </h1>
          <p className="mt-5 text-pretty text-lg leading-relaxed text-muted-foreground">
            Camera-based detection with guard-initiated recording and instant
            alarms — privacy-first and response-ready.
          </p>

          {/* CTAs */}
          <div className="mt-8 flex flex-wrap items-center gap-4">
            <a
              href="#contact"
              className="rounded-pill bg-primary px-7 py-3 text-sm font-semibold text-primary-foreground shadow-sm transition-opacity hover:opacity-90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
            >
              Request a demo
            </a>
            <a
              href="#demo"
              className="flex items-center gap-2 rounded-pill border border-border bg-card px-6 py-3 text-sm font-semibold text-foreground shadow-sm transition-colors hover:bg-secondary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
            >
              <Play className="h-4 w-4 fill-primary text-primary" />
              Watch 30s demo
            </a>
          </div>

          {/* Trust line */}
          <div className="mt-8 flex flex-wrap items-center gap-5 text-xs text-muted-foreground">
            <span className="flex items-center gap-1.5">
              <ShieldCheck className="h-4 w-4 text-primary" />
              Trusted in 120+ communities
            </span>
            <span className="flex items-center gap-1.5">
              <Clock className="h-4 w-4 text-primary" />
              Avg response time -38%
            </span>
            <span className="flex items-center gap-1.5">
              <Lock className="h-4 w-4 text-primary" />
              End-to-end encrypted clips
            </span>
          </div>
        </div>

        {/* Hero visual */}
        <div className="relative w-full max-w-lg flex-shrink-0 lg:max-w-md xl:max-w-lg">
          <div className="overflow-hidden rounded-2xl border border-border bg-card shadow-lg">
            <Image
              src="/hero-security.jpg"
              alt="Isometric view of a smartphone and security camera overlay showing the SafeSight monitoring dashboard"
              width={640}
              height={480}
              className="h-auto w-full object-cover"
              priority
            />
          </div>
          {/* Floating badge */}
          <div className="absolute -bottom-4 -left-4 flex items-center gap-2 rounded-xl border border-border bg-card px-4 py-2.5 shadow-md">
            <span className="relative flex h-2.5 w-2.5">
              <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-green-400 opacity-75" />
              <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-green-500" />
            </span>
            <span className="text-xs font-medium text-foreground">
              Live monitoring active
            </span>
          </div>
        </div>
      </div>
    </section>
  )
}
