import { Cpu, Hand, Bell, FileDown, BarChart3 } from "lucide-react"

const features = [
  {
    icon: Cpu,
    title: "Automated Detection",
    description:
      "AI-powered analysis spots altercations the moment they happen on your existing camera feeds.",
  },
  {
    icon: Hand,
    title: "One-tap Guard Report",
    description:
      "Guards can manually report incidents, start recording, and trigger actions with a single tap.",
  },
  {
    icon: Bell,
    title: "Instant Notifications",
    description:
      "Push alerts reach your security team in real time — on mobile, desktop, or in-app.",
  },
  {
    icon: FileDown,
    title: "Secure Evidence Export",
    description:
      "Export encrypted incident clips for law enforcement, insurance, or internal review.",
  },
  {
    icon: BarChart3,
    title: "Incident Analytics",
    description:
      "Track trends, response times, and hotspots with built-in analytics dashboards.",
  },
]

export function Features() {
  return (
    <section id="features" className="bg-card py-16 md:py-24">
      <div className="mx-auto max-w-6xl px-6">
        <div className="mx-auto max-w-2xl text-center">
          <p className="text-sm font-semibold uppercase tracking-widest text-primary">
            Features
          </p>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight text-foreground md:text-4xl">
            Everything you need for safer communities
          </h2>
        </div>

        <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {features.map((item) => (
            <div
              key={item.title}
              className="group rounded-2xl border border-border bg-background p-7 shadow-sm transition-shadow hover:shadow-md"
            >
              <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-primary/10">
                <item.icon className="h-5 w-5 text-primary" />
              </div>
              <h3 className="mt-5 text-base font-semibold text-foreground">
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
