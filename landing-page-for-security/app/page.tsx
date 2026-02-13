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
        
        {/* Demo Request Section */}
        <section className="bg-primary py-16 md:py-24">
          <div className="mx-auto max-w-6xl px-6 lg:px-8">
            <div className="text-center">
              <h2 className="text-3xl font-bold tracking-tight text-primary-foreground md:text-4xl mb-4">
                Request Full Demo Access
              </h2>
              <p className="text-lg text-primary-foreground/90 max-w-2xl mx-auto mb-8">
                Experience the complete SafeSight security platform with live monitoring, AI detection, and response capabilities.
              </p>
              
              <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <a
                  href="http://127.0.0.1:8000/auth/login"
                  className="inline-flex items-center justify-center rounded-full bg-primary-foreground px-8 py-4 text-lg font-semibold text-primary transition-all hover:bg-primary/90"
                >
                  📹 Try Live Demo
                </a>
                <a
                  href="http://127.0.0.1:8000/auth/login"
                  className="inline-flex items-center justify-center rounded-full border-2 border-primary-foreground px-8 py-4 text-lg font-semibold text-primary-foreground transition-all hover:bg-primary-foreground hover:text-primary-foreground"
                >
                  🔐 Request Full Access
                </a>
              </div>
              
              <p className="text-sm text-primary-foreground/70 mt-6">
                Demo access provides limited functionality. Full access requires authentication.
              </p>
            </div>
          </div>
        </section>
        
        <ContactForm />
        <FAQ />
      </main>
      <Footer />
    </div>
  )
}
