// Primeiramente, importamos os componentes necessários de outros arquivos.
// Isso inclui componentes para Avatar, Botão e vários componentes relacionados ao menu dropdown.
import {
  Avatar,
  AvatarFallback,
  AvatarImage,
} from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

// Definição do componente UserNav como uma função React.
export function UserNav() {
  // A renderização do componente começa aqui.
  return (
    // O componente DropdownMenu é o contêiner principal para o nosso menu de usuário.
    <DropdownMenu>
      {/* DropdownMenuTrigger define o elemento que, quando clicado, abrirá o menu dropdown.
          Usamos o componente Button como filho (asChild), personalizado com classes CSS. */}
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" className="relative h-8 w-8 rounded-full">
          {/* O Avatar é mostrado no botão que aciona o dropdown.
              Contém uma imagem com fallback para iniciais, caso a imagem não carregue. */}
          <Avatar className="h-8 w-8">
            <AvatarImage src="/avatars/01.png" alt="@shadcn" />
            <AvatarFallback>EA</AvatarFallback>
          </Avatar>
        </Button>
      </DropdownMenuTrigger>
      
      {/* DropdownMenuContent contém todo o conteúdo do nosso menu dropdown.
          Aqui definimos sua largura, alinhamento e outras propriedades CSS. */}
      <DropdownMenuContent className="w-56" align="end" forceMount>
        {/* DropdownMenuLabel é usado para mostrar um cabeçalho no menu dropdown,
            neste caso, o nome e e-mail do usuário. */}
        <DropdownMenuLabel className="font-normal">
          <div className="flex flex-col space-y-1">
            <p className="text-sm font-medium leading-none">Enya Arruda</p>
            <p className="text-xs leading-none text-muted-foreground">
              enyaarruda@example.com
            </p>
          </div>
        </DropdownMenuLabel>

        {/* Exemplo de como itens do menu são organizados. Cada item do menu pode ter um atalho.
            Estes itens foram comentados para demonstração e podem ser descomentados para uso.
            
        <DropdownMenuSeparator />
        <DropdownMenuGroup>
          <DropdownMenuItem>
            Profile
            <DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
          </DropdownMenuItem>
          <DropdownMenuItem>
            Billing
            <DropdownMenuShortcut>⌘B</DropdownMenuShortcut>
          </DropdownMenuItem>
          <DropdownMenuItem>
            Settings
            <DropdownMenuShortcut>⌘S</DropdownMenuShortcut>
          </DropdownMenuItem>
          <DropdownMenuItem>New Team</DropdownMenuItem>
        </DropdownMenuGroup>
        <DropdownMenuSeparator />
        <DropdownMenuItem>
          Log out
          <DropdownMenuShortcut>⇧⌘Q</DropdownMenuShortcut>
        </DropdownMenuItem> */}
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
