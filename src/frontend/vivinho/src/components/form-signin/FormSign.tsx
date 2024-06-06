// Utiliza o ambiente do cliente em vez de um servidor
"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { Form, useForm } from "react-hook-form"
import { z } from "zod"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Label } from "../ui/label"
import Link from "next/link"
import { Checkbox } from "@/components/ui/checkbox"
import { useState } from "react"

const formSchema = z.object({
  nome: z.string().min(1, {
    message: "Nome é obrigatório",
  }),
  endereco: z.string().min(1, {
    message: "Endereço é obrigatório",
  }),
  email: z.string().email({
    message: "Email inválido",
  }),
  password: z.string().min(6, {
    message: "Senha deve ter no mínimo 6 caracteres",
  }),
})


export default function FormLogin() {
  const [rememberChecked, setRememberChecked] = useState(false)

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      email: "",
      password: "",
      nome: "",
      endereco: ""
    },
  })

  function handleRememberChecked() {
    setRememberChecked(!rememberChecked);
  }

  function onSubmit(data: z.infer<typeof formSchema>) {
    console.log(data)
  }

  return (
    <form
      className="space-y-4 md:space-y-6"
      onSubmit={form.handleSubmit(onSubmit)}
    >
      <div>
        <Label htmlFor="nome"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Nome</Label>
        {
          form.formState.errors.nome && (
            <p className="text-sm text-purple-500 dark:text-red-400 mb-2">
              {`* ${form.formState.errors.nome.message}`}
            </p>
          )
        }
        <Input
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Maria Lima"
          id="nome"
          {...form.register("nome")}
        />
      </div>
      <div>
        <Label htmlFor="email"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >E-mail</Label>
        {
          form.formState.errors.email && (
            <p className="text-sm text-purple-500 dark:text-red-400 mb-2">
              {`* ${form.formState.errors.email.message}`}
            </p>
          )
        }
        <Input
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="exemplo@empresa.com"
          id="email"
          {...form.register("email")}
        />
      </div>
      <div>
        <Label htmlFor="endereco"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Endereço</Label>
        {
          form.formState.errors.endereco && (
            <p className="text-sm text-purple-500 dark:text-red-400 mb-2">
              {`* ${form.formState.errors.endereco.message}`}
            </p>
          )
        }
        <Input
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="Rua XX, 81"
          id="endereco"
          {...form.register("endereco")}
        />
      </div>
      <div>
        <Label htmlFor="password"
          className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >Senha</Label>
        {
          form.formState.errors.password && (
            <p className="text-sm text-purple-500 dark:text-red-400 mb-2">
              {`* ${form.formState.errors.password.message}`}
            </p>
          )
        }
        <Input
          className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          placeholder="••••••••"
          id="password"
          type="password"
          {...form.register("password")}
        />
      </div>
      
      <div className="flex items-center justify-between">
        <div className="flex items-start">
          <div className="flex items-center h-5">
            <Checkbox
              checked={rememberChecked}
              id="remember"
              aria-describedby="remember"
              className={`w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 
                  dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 
                  dark:ring-offset-gray-800 peer-checked:border-transparent peer-checked:text-white 
                  peer-checked:ring-0 peer-checked:ring-offset-0`}
              onCheckedChange={handleRememberChecked}
            />
          </div>
          <div className="ml-3 text-sm">
            <label htmlFor="remember" className="text-gray-400 dark:text-gray-300">Lembre de mim</label>
          </div>
        </div>
      </div>
      <Button
        className="w-full text-white bg-purple-700 hover:bg-purple-700 focus:ring-4 focus:outline-none focus:ring-purple-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-purple-700 dark:hover:bg-purple-700 dark:focus:ring-purple-900 mt-6"
        type="submit"
      >
        Entrar
      </Button>
      <p className="text-sm font-light text-gray-500 dark:text-gray-400">
        Já tem um conta? <Link href={"/login"} className="font-medium text-purple-700 hover:underline dark:text-purple-600">Login</Link>
      </p>

    </form>
  )
}