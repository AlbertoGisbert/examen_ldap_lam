def generar_alumno(nombre, apellido, clase):

return {
	'dn': f"uid={nombre.lower()}.{apellido.lower()}, ou=alumnos, dc=example, dc=com",
	'objectClass': ['inetOrgPerson', 'organizationalPerson', 'person'],
	'uid': f"{nombre.lower()}-{apellido.lower()}",
	'cn': f"{nombre} {apellido}",
	'sn': apellido,
	'giveName': nombre,
	'mail': f"{nombre.lower()}.{apellido.lower()}@example.com",
	'clase': clase
}
def create_organizational_unit_ldif(filename, ou_name, base_dn):
    """Creates an LDIF file for an organizational unit."""
	alumnos = []
	nombres = ["Juan", "Ana", "Luis"]
	apellidos = ["Gomez", "Perez", "Lopez"]
    ldif_content = f"""# organisational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}
"""

    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Example usage:
filename = "ou.ldif"  # Name of the LDIF file
ou_name = "directores"                   # Name of the organizational unit
base_dn = "dc=example,dc=org"   # Your base DN (replace with your actual DN)

create_organizational_unit_ldif(filename, ou_name, base_dn)

