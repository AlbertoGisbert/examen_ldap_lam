def create_organizational_unit_ldif(filename, ou_list, base_dn):
    """Generates an LDIF file for a list of organizational units."""

    try:
        with open(filename, "w") as f:
            for ou_name in ou_list:
                ldif_content = f"""# organisational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}
"""
                f.write(ldif_content)
                f.write("\n")  # Add an extra line between entries for readability

        print(f"LDIF file '{filename}' created successfully with {len(ou_list)} organizational units.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Example usage:
filename = "ou_list.ldif"  # Name of the LDIF file
ou_list = ["directores", "profesores", "alumnos"]  # List of organizational units (groups)
base_dn = "dc=example,dc=org"  # Your base DN (replace with your actual DN)

# Llamada a la función con la lista de unidades organizativas
filename = "ou_list.ldif"  # Nombre del archivo LDIF a crear
ou_list = ["1ESOA", "1ESOB", "1ESOC", "1ESOD"]  # Lista de unidades organizativas
base_dn = "dc=example,dc=org"  # Base DN, debe ser ajustado a tu entorno de dominio

create_organizational_unit_ldif(filename, ou_list, base_dn)

create_organizational_unit_ldif(filename, ou_list, base_dn)
