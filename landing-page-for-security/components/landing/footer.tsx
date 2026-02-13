import { Shield } from "lucide-react"

const links = {
  Product: ["Features", "Pricing", "Integrations", "Changelog"],
  Company: ["About", "Blog", "Careers", "Press"],
  Legal: ["Privacy Policy", "Terms of Service", "Cookie Policy"],
  Support: ["Help Center", "Contact", "Status", "API Docs"],
}

export function Footer() {
  return (
    <footer className="border-t border-border bg-card">
      <div className="mx-auto max-w-6xl px-6 py-12">
        <div className="grid gap-10 md:grid-cols-5">
          {/* Brand */}
          <div className="md:col-span-1">
            <a href="#" className="flex items-center gap-2" aria-label="SafeSight home">
              <Shield className="h-6 w-6 text-primary" />
              <span className="text-base font-bold text-foreground">SafeSight</span>
            </a>
            <p className="mt-3 text-xs leading-relaxed text-muted-foreground">
              Camera-based fight detection. Privacy-first. Response-ready.
            </p>
          </div>

          {/* Link columns */}
          {Object.entries(links).map(([heading, items]) => (
            <div key={heading}>
              <h4 className="text-sm font-semibold text-foreground">{heading}</h4>
              <ul className="mt-3 flex flex-col gap-2.5">
                {items.map((item) => (
                  <li key={item}>
                    <a
                      href="#"
                      className="text-sm text-muted-foreground transition-colors hover:text-foreground"
                    >
                      {item}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="mt-10 border-t border-border pt-6 text-center text-xs text-muted-foreground">
          <p>
            {"© 2026 SafeSight Inc. All rights reserved. Need accessibility help? "}
            <a href="mailto:access@safesight.io" className="underline hover:text-foreground">
              access@safesight.io
            </a>
          </p>
        </div>
      </div>
    </footer>
  )
}
