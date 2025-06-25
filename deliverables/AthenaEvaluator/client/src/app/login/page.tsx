"use client";
import { Button, Card, CardContent, CardHeader, Input } from "@mui/material";
import { login } from "./util";
import { useRouter } from "next/navigation";

import { useState } from "react";

export default function Login() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log({ email, password });

    try {
      await login(email, password);
      router.push("/");
    } catch (error) {
      console.error("Erro ao fazer login:", error);
      alert(
        "Erro ao fazer login. Verifique suas credenciais e tente novamente."
      );
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <Card className="w-full max-w-sm shadow-lg rounded-2xl">
        <CardHeader>
          <p className="text-center text-xl">Login</p>
        </CardHeader>
        <CardContent>
          <form
            onSubmit={handleSubmit}
            // className="space-y-4"
          >
            <div>
              {/* <label htmlFor="email" className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400">Email</label> */}
              <Input
                type="email"
                placeholder="Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                // className="pl-10"
                className="w-full"
                required
              />
            </div>
            <div>
              <Input
                type="password"
                placeholder="Senha"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                // className="pl-10"
                className="w-full"
                required
              />
            </div>
            <Button type="submit" className="w-full">
              Entrar
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
