// Importação de componentes e recursos necessários
import Image from "next/image";
import vivoLogo from "../../assets/img/Logo_VIVO.png";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import FormLogin from "@/components/form-login/FormLogin";

// Componente da página de login
export default function LoginPage() {
  return (
    // Container principal da página
    <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0 bg-gray-50 dark:bg-gray-900">
      
      {/* // Logo da empresa */}
      <div className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
        <Image src={vivoLogo} alt="Vivo" height={40} />
      </div>

      {/* // Card contendo o formulário de login */}
      <Card className="w-full bg-white rounded-lg shadow border-0 dark:border md:mt-0 sm:max-w-md xl:p-2 dark:bg-gray-800 dark:border-gray-700">
        <CardHeader>
          {/* // Título da página de login */}
          <CardTitle className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
            Faça login em sua conta
          </CardTitle>
        </CardHeader>
        <CardContent>
          {/* // Componente do formulário de login */}
          <FormLogin />
        </CardContent>
      </Card>
    </div>
  );
}
