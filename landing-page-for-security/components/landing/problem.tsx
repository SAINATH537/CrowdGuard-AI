import { AlertTriangle, Clock, ShieldOff } from "lucide-react"

const problems = [
  {
    icon: AlertTriangle,
    title: "Unreported incidents",
    description:
      "Many fights captured on cameras go unreported because no one is monitoring in real time.",
  },
  {
    icon: Clock,
    title: "Slow responses",
    description:
      "By the time an incident is noticed and reported, the situation has already escalated.",
  },
  {
    icon: ShieldOff,
    title: "Unsafe spaces",
    description:
      "Without immediate detection and response tools, communities remain vulnerable.",
  },
]

export function Problem() {
  return (
    <section className="bg-card py-16 md:py-24">
      <div className="mx-auto max-w-6xl px-6">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-balance text-3xl font-bold tracking-tight text-foreground md:text-4xl">
            Unreported incidents. Slow responses. Unsafe spaces.
          </h2>
          <p className="mt-4 text-pretty leading-relaxed text-muted-foreground">
            Many fights captured on cameras go unreported because no one is
            watching in real time. Response delays put people at risk and leave
            communities feeling unsafe.
          </p>
        </div>

        <div className="mt-12 grid gap-8 md:grid-cols-3">
          {problems.map((item) => (
            <div
              key={item.title}
              className="flex flex-col items-center rounded-2xl border border-border bg-background p-8 text-center shadow-sm"
            >
              <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-destructive/10">
                <item.icon className="h-6 w-6 text-destructive" />
              </div>
              <h3 className="mt-5 text-lg font-semibold text-foreground">
                {item.title}
              </h3>
              <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
                {item.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
