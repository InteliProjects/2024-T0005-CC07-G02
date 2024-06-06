// Importações necessárias: Image para imagens otimizadas, logo da Vivo, componentes de Card e FormSign para o formulário de cadastro.

import Image from "next/image";
import vivoLogo from "../../assets/img/Logo_VIVO.png";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import FormLogin from "@/components/form-signin/FormSign"; // Note: O nome importado FormLogin é inconsistente com o export FormSign.

// Componente funcional para a página de login/cadastro.
export default function LoginPage() {
  return (
    // Container geral para centralização e estilo da página.
    <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0 bg-gray-50 dark:bg-gray-900">
      
      {/* // Exibição do logo com componente Image do Next.js para otimização. */}
      <div className="flex items-center mb-6 text-2xl font-semibold text-gray-900 dark:text-white">
        <Image src={vivoLogo} alt="Vivo" height={40} />
      </div>

      {/* // Card para conter os elementos do formulário de cadastro, com adaptações para tema escuro. */}
      <Card className="w-full bg-white rounded-lg shadow border-0 dark:border md:mt-0 sm:max-w-md xl:p-2 dark:bg-gray-800 dark:border-gray-700">
        <CardHeader>
          {/* // Título do card, indicando a ação de cadastro ao usuário. */}
          <CardTitle className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
            Faça seu cadastro
          </CardTitle>
        </CardHeader>
        <CardContent>
          {/* // Incorporação do formulário de cadastro. */}
          <FormLogin /> 
        </CardContent>
      </Card>
    </div>
  );
}
