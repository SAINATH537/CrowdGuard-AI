import { ScanEye, UserCheck, Siren } from "lucide-react"

const steps = [
  {
    icon: ScanEye,
    step: "01",
    title: "Detect",
    description:
      "AI continuously analyzes your existing camera feeds to identify potential altercations in real time.",
  },
  {
    icon: UserCheck,
    step: "02",
    title: "Verify",
    description:
      "Security guards receive an instant alert and can verify the incident with one tap on their device.",
  },
  {
    icon: Siren,
    step: "03",
    title: "Respond",
    description:
      "Trigger alarms, start recording, and notify responders — all within seconds of detection.",
  },
]

export function HowItWorks() {
  return (
    <section id="how-it-works" className="py-16 md:py-24">
      <div className="mx-auto max-w-6xl px-6">
        <div className="mx-auto max-w-2xl text-center">
          <p className="text-sm font-semibold uppercase tracking-widest text-primary">
            How it works
          </p>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight text-foreground md:text-4xl">
            Three steps to safer spaces
          </h2>
        </div>

        <div className="relative mt-16 grid gap-8 md:grid-cols-3">
          {/* Connecting line (desktop) */}
          <div
            className="absolute left-[16.66%] right-[16.66%] top-10 hidden h-px bg-border md:block"
            aria-hidden="true"
          />

          {steps.map((item) => (
            <div
              key={item.step}
              className="relative flex flex-col items-center text-center"
            >
              <div className="relative z-10 flex h-20 w-20 items-center justify-center rounded-2xl border border-border bg-card shadow-sm">
                <item.icon className="h-8 w-8 text-primary" />
              </div>
              <span className="mt-4 text-xs font-bold uppercase tracking-widest text-primary">
                Step {item.step}
              </span>
              <h3 className="mt-2 text-xl font-semibold text-foreground">
                {item.title}
              </h3>
              <p className="mt-2 max-w-xs text-sm leading-relaxed text-muted-foreground">
                {item.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
