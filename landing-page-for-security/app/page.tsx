import { Navbar } from "@/components/landing/navbar"
import { Hero } from "@/components/landing/hero"
import { Problem } from "@/components/landing/problem"
import { HowItWorks } from "@/components/landing/how-it-works"
import { Features } from "@/components/landing/features"
import { Demo } from "@/components/landing/demo"
import { SocialProof } from "@/components/landing/social-proof"
import { Privacy } from "@/components/landing/privacy"
import { ContactForm } from "@/components/landing/contact-form"
import { FAQ } from "@/components/landing/faq"
import { Footer } from "@/components/landing/footer"

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <Navbar />
      <main>
        <Hero />
        <Problem />
        <HowItWorks />
        <Features />
        <Demo />
        <SocialProof />
        <Privacy />
        <ContactForm />
        <FAQ />
      </main>
      <Footer />
    </div>
  )
}
