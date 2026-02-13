import { Quote } from "lucide-react"

const stats = [
  { value: "120+", label: "Communities protected" },
  { value: "-38%", label: "Avg. response time reduction" },
  { value: "99.5%", label: "Uptime guarantee" },
]

const testimonials = [
  {
    quote:
      "Since deploying SafeSight, our incident response time dropped by nearly 40%. Guards feel empowered and residents feel safer.",
    role: "Head of Security",
    org: "Urban Residential Complex",
  },
  {
    quote:
      "The one-tap reporting is a game changer. No more radio confusion — everything is documented and timestamped automatically.",
    role: "Operations Manager",
    org: "Mixed-Use Development",
  },
  {
    quote:
      "We needed a privacy-first solution that worked with our existing cameras. SafeSight delivered on every front.",
    role: "Campus Safety Director",
    org: "Education Institution",
  },
]

export function SocialProof() {
  return (
    <section className="bg-card py-16 md:py-24">
      <div className="mx-auto max-w-6xl px-6">
        {/* Stats */}
        <div className="grid gap-6 md:grid-cols-3">
          {stats.map((stat) => (
            <div
              key={stat.label}
              className="flex flex-col items-center rounded-2xl border border-border bg-background p-8 text-center shadow-sm"
            >
              <span className="text-4xl font-bold text-primary">
                {stat.value}
              </span>
              <span className="mt-2 text-sm text-muted-foreground">
                {stat.label}
              </span>
            </div>
          ))}
        </div>

        {/* Testimonials */}
        <div className="mt-16">
          <h2 className="text-center text-2xl font-bold tracking-tight text-foreground md:text-3xl">
            What our customers say
          </h2>
          <div className="mt-10 grid gap-6 md:grid-cols-3">
            {testimonials.map((t) => (
              <div
                key={t.role}
                className="flex flex-col rounded-2xl border border-border bg-background p-7 shadow-sm"
              >
                <Quote className="h-5 w-5 text-primary/40" />
                <p className="mt-4 flex-1 text-sm leading-relaxed text-foreground">
                  {t.quote}
                </p>
                <div className="mt-6 border-t border-border pt-4">
                  <p className="text-sm font-semibold text-foreground">
                    {t.role}
                  </p>
                  <p className="text-xs text-muted-foreground">{t.org}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
