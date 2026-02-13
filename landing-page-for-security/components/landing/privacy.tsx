import { Lock, CalendarClock, Users, HardDrive } from "lucide-react"

const items = [
  {
    icon: Lock,
    title: "End-to-end encryption",
    description: "All video clips and incident data are encrypted in transit and at rest.",
  },
  {
    icon: CalendarClock,
    title: "30-day default retention",
    description: "Footage is automatically purged after 30 days unless flagged for review.",
  },
  {
    icon: Users,
    title: "Role-based access",
    description: "Only authorized personnel can view, export, or manage incident data.",
  },
  {
    icon: HardDrive,
    title: "Local-first recording opt-in",
    description: "Choose to keep recordings on-premise for full data sovereignty.",
  },
]

export function Privacy() {
  return (
    <section id="privacy" className="py-16 md:py-24">
      <div className="mx-auto max-w-6xl px-6">
        <div className="mx-auto max-w-2xl text-center">
          <p className="text-sm font-semibold uppercase tracking-widest text-primary">
            Privacy & Security
          </p>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight text-foreground md:text-4xl">
            Built with privacy at the core
          </h2>
          <p className="mt-4 text-pretty leading-relaxed text-muted-foreground">
            Your data, your control. SafeSight meets the highest standards for
            data protection and access management.
          </p>
        </div>

        <div className="mt-12 grid gap-6 sm:grid-cols-2">
          {items.map((item) => (
            <div
              key={item.title}
              className="flex gap-5 rounded-2xl border border-border bg-card p-7 shadow-sm"
            >
              <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-primary/10">
                <item.icon className="h-5 w-5 text-primary" />
              </div>
              <div>
                <h3 className="text-base font-semibold text-foreground">
                  {item.title}
                </h3>
                <p className="mt-1 text-sm leading-relaxed text-muted-foreground">
                  {item.description}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
