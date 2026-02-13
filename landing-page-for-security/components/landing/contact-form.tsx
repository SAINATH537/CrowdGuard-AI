"use client"

import { useState } from "react"
import { CheckCircle2 } from "lucide-react"

export function ContactForm() {
  const [submitted, setSubmitted] = useState(false)

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault()
    setSubmitted(true)
  }

  return (
    <section id="contact" className="bg-primary py-16 md:py-24">
      <div className="mx-auto max-w-2xl px-6">
        <div className="text-center">
          <h2 className="text-balance text-3xl font-bold tracking-tight text-primary-foreground md:text-4xl">
            Ready to protect your community?
          </h2>
          <p className="mt-3 text-primary-foreground/80">
            Request a personalized demo and see SafeSight in action.
          </p>
        </div>

        {!submitted ? (
          <form
            onSubmit={handleSubmit}
            className="mt-10 rounded-2xl bg-card p-8 shadow-xl"
          >
            <div className="grid gap-5 sm:grid-cols-2">
              <div className="sm:col-span-2">
                <label
                  htmlFor="org"
                  className="mb-1.5 block text-sm font-medium text-foreground"
                >
                  Organization <span className="text-destructive">*</span>
                </label>
                <input
                  id="org"
                  name="organization"
                  type="text"
                  required
                  className="w-full rounded-lg border border-input bg-background px-4 py-2.5 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-ring/20"
                  placeholder="Acme Properties"
                  suppressHydrationWarning
                />
              </div>
              <div>
                <label
                  htmlFor="name"
                  className="mb-1.5 block text-sm font-medium text-foreground"
                >
                  Name <span className="text-destructive">*</span>
                </label>
                <input
                  id="name"
                  name="name"
                  type="text"
                  required
                  className="w-full rounded-lg border border-input bg-background px-4 py-2.5 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-ring/20"
                  placeholder="Jane Doe"
                  suppressHydrationWarning
                />
              </div>
              <div>
                <label
                  htmlFor="email"
                  className="mb-1.5 block text-sm font-medium text-foreground"
                >
                  Email <span className="text-destructive">*</span>
                </label>
                <input
                  id="email"
                  name="email"
                  type="email"
                  required
                  className="w-full rounded-lg border border-input bg-background px-4 py-2.5 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-ring/20"
                  placeholder="jane@acme.com"
                  suppressHydrationWarning
                />
              </div>
              <div>
                <label
                  htmlFor="phone"
                  className="mb-1.5 block text-sm font-medium text-foreground"
                >
                  Phone <span className="text-muted-foreground">(optional)</span>
                </label>
                <input
                  id="phone"
                  name="phone"
                  type="tel"
                  className="w-full rounded-lg border border-input bg-background px-4 py-2.5 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-ring/20"
                  placeholder="+1 (555) 000-0000"
                  suppressHydrationWarning
                />
              </div>
              <div>
                <label
                  htmlFor="role"
                  className="mb-1.5 block text-sm font-medium text-foreground"
                >
                  Role <span className="text-destructive">*</span>
                </label>
                <select
                  id="role"
                  name="role"
                  required
                  className="w-full rounded-lg border border-input bg-background px-4 py-2.5 text-sm text-foreground focus:border-primary focus:outline-none focus:ring-2 focus:ring-ring/20"
                  defaultValue=""
                  suppressHydrationWarning
                >
                  <option value="" disabled>
                    Select your role
                  </option>
                  <option>Security Manager</option>
                  <option>Property Manager</option>
                  <option>Operations Director</option>
                  <option>IT Administrator</option>
                  <option>Other</option>
                </select>
              </div>
            </div>

            <button
              type="submit"
              className="mt-6 w-full rounded-pill bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground shadow-sm transition-opacity hover:opacity-90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
              suppressHydrationWarning
            >
              Request demo
            </button>
          </form>
        ) : (
          <div className="mt-10 flex flex-col items-center rounded-2xl bg-card p-10 text-center shadow-xl">
            <CheckCircle2 className="h-12 w-12 text-green-500" />
            <h3 className="mt-4 text-xl font-semibold text-foreground">
              Thanks for your interest!
            </h3>
            <p className="mt-2 text-sm text-muted-foreground">
              {"We'll email available demo slots within 24 hours."}
            </p>
          </div>
        )}
      </div>
    </section>
  )
}
