// Importação de tipos e funções do Next.js para manipulação de metadados e fontes.
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css"; // Importação de estilos globais.

// Configuração da fonte Inter com subconjunto latino, usando a nova API de fontes do Next.js.
const inter = Inter({ subsets: ["latin"] });

// Definição de metadados globais para a aplicação, utilizável em toda a aplicação.
export const metadata: Metadata = {
  title: "Vivinho", // Título padrão da aplicação.
  description: "Aplicação Web Vivinho", // Descrição da aplicação.
};

// Componente RootLayout para envolver toda a aplicação, definindo estruturas HTML básicas e estilos.
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode; // Tipagem para os filhos do componente, permitindo qualquer elemento React válido.
}>) {
  return (
    // Estrutura básica do documento HTML.
    <html lang="pt"> 
    {/* // Definição do idioma do documento para inglês. */}
      <body className={inter.className}>{children}</body> 
      {/* // Uso da fonte Inter no corpo do documento, envolvendo todos os elementos filhos. */}
    </html>
  );
}
