"use client"

import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion"

const faqs = [
  {
    q: "Who owns the recorded footage?",
    a: "You do. All footage is stored under your organization's account and you retain full ownership and control over it at all times.",
  },
  {
    q: "How do you handle false positives?",
    a: "Our AI model is continuously trained to minimize false positives. Guards can quickly dismiss false alerts with one tap, and feedback is used to improve detection accuracy.",
  },
  {
    q: "What hardware do I need?",
    a: "SafeSight works with your existing IP security cameras — no proprietary hardware required. We support RTSP and ONVIF-compatible cameras.",
  },
  {
    q: "How does the guard alarm work?",
    a: "When an incident is detected or reported, guards receive a push notification. They can verify, start recording, and trigger a site alarm with a single tap on the mobile app.",
  },
  {
    q: "How is user privacy protected?",
    a: "All clips are end-to-end encrypted. We offer 30-day auto-deletion, role-based access controls, and optional local-first storage to ensure compliance with privacy regulations.",
  },
  {
    q: "What does the onboarding timeline look like?",
    a: "Most organizations are up and running within 1–2 weeks. Our team handles camera integration, staff training, and initial configuration at no extra cost.",
  },
]

export function FAQ() {
  return (
    <section id="faq" className="py-16 md:py-24">
      <div className="mx-auto max-w-3xl px-6">
        <div className="text-center">
          <p className="text-sm font-semibold uppercase tracking-widest text-primary">
            FAQ
          </p>
          <h2 className="mt-3 text-balance text-3xl font-bold tracking-tight text-foreground md:text-4xl">
            Frequently asked questions
          </h2>
        </div>

        <Accordion type="single" collapsible className="mt-10">
          {faqs.map((faq, i) => (
            <AccordionItem key={i} value={`faq-${i}`}>
              <AccordionTrigger className="text-left text-base font-medium text-foreground">
                {faq.q}
              </AccordionTrigger>
              <AccordionContent className="text-sm leading-relaxed text-muted-foreground">
                {faq.a}
              </AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
      </div>
    </section>
  )
}
