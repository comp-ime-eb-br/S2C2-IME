export async function login(email: string, password: string) {
  if (!email || !password) {
    alert("Por favor, preencha o email e a senha.");
    return;
  }

  const payload = { email, password };

  try {
    console.log("Fazendo login...", process.env.LOGIN_URL);
    const response = await fetch(
      `${process.env.LOGIN_URL || "https://app.fairdatapoint.org"}/tokens`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify(payload),
      }
    );

    if (!response.ok) {
      throw new Error(`Erro ao fazer login: ${response.statusText}`);
    }

    const data = await response.json();

    localStorage.setItem(
      "auth",
      JSON.stringify({ session: { token: data.token } })
    );
    alert("Login realizado com sucesso!");
    // window.location.href = 'tests.html'; // Redireciona para a página principal após o login
  } catch (error) {
    console.error("Erro ao fazer login:", error);
    alert("Erro ao fazer login. Verifique suas credenciais e tente novamente.");
    throw error;
  }
}
