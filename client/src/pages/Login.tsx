import { TextInput, Grid, Container, Title, Button, PasswordInput, Flex, Anchor } from "@mantine/core";
import { useForm } from "@mantine/form";

function LogInPage() {
  const form = useForm({
    mode: "uncontrolled", initialValues: {
      email: "", password: ""
    }
  });

  return (
    <Container h="100vh" >
      <Grid h="100vh" grow gutter="xl" display="grid" align="center">
        <Grid.Col span="auto">
          SVG
        </Grid.Col>
        <Grid.Col span={4}>
          <Flex align="center" justify="center" direction="column" rowGap="sm" p="xs" pb="xl" my="lg" style={{ border: "1px solid #969696", borderRadius: "5px" }}>
            <Title order={1} style={{ textShadow: "3px 0px #7D19E1, 6px 0px #E0D0FF", userSelect: "none" }} >Veem</Title>
            <form onSubmit={(evt) => { evt.preventDefault(); console.log(form.getValues()) }}>
              <Flex direction="column" rowGap="xs">
                <TextInput type="email" required autoFocus autoComplete="false" placeholder="Correo Electrónico" key={form.key('email')}
                  {...form.getInputProps('email')} />
                <PasswordInput placeholder="Contraseña" key={form.key('password')}
                  {...form.getInputProps('password')} />
                <Button type="submit" fullWidth>Ingresar</Button>
              </Flex>
            </form>
          </Flex>
          <Flex px="lg" py="xs" style={{ border: "1px solid #969696", borderRadius: "5px" }}>
            ¿No tienes cuentas? <Anchor href="/register" ml="xs">Registrate</Anchor>
          </Flex>
        </Grid.Col>
      </Grid>
    </Container>
  )
}

export default LogInPage