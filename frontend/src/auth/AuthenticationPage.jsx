import "react"
import {SignIn, SignUp, SignedIn, SignedOut} from "@clerk/clerk-react"

export function AuthenticationPage(){
  return <div className="auth-container">
    <SignedOut>
      <SignIn routing="path" path="/sign-in" /> {/*Se o usuário estiver na página 'sign-in', ele irá ser redirecionado para a página de sign-in */}
      <SignUp routing="path" path="/sign-up" /> {/*Se o usuário estiver na página 'sign-up', ele irá ser redirecionado para a página de sign-up */}
    </SignedOut>
    <SignedIn>
      <div className="redirect-message">
        <p> You are already signed in!</p>
      </div>
    </SignedIn>
  </div>
}