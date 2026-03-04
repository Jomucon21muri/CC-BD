# Expansión temporal Capítulo 3

## Contenido a agregar después de sección 3.3 (antes de Regiones)

## 3.4. Beneficios y Desventajas de Cloud Computing

### Beneficios Principales

#### 1. Integración Probada de Servicios de Red

**Ventaja:** La tecnología cloud computing se integra con mayor facilidad y rapidez con el resto de aplicaciones empresariales.

```python
# Ejemplo: Integración fácil de servicios AWS
import boto3

# Integrar múltiples servicios en mismo ecosistema
s3 = boto3.client('s3')           # Almacenamiento
lambda_client = boto3.client('lambda')  # Computación serverless
sns = boto3.client('sns')         # Notificaciones
sqs = boto3.client('sqs')         # Colas de mensajes

# Todo integrado nativamente, APIs consistentes
# Sin necesidad de middleware complejo
```

#### 2. Prestación de Servicios a Nivel Mundial

**Ventaja:** Infraestructuras que proporcionan:
- ✅ Mayor capacidad de adaptación
- ✅ Recuperación completa de pérdida de datos (backups automáticos)
- ✅ Reducción al mínimo de tiempos de inactividad
- ✅ Alta disponibilidad global

**Mecanismo:**
Ante eventualidades de fallas, el cloud re-asigna automáticamente nuevas VMs para las aplicaciones.

```
Ejemplo: Aplicación web en 3 regiones

       Usuario España          Usuario USA          Usuario Asia
            ↓                      ↓                    ↓
    EU-West-1 (Irlanda)    US-East-1 (Virginia)   AP-Southeast-1 (Singapur)
         Server 1               Server 2              Server 3
         
Si Server 1 falla:
→ Route 53 (DNS) redirige automáticamente a Server 2
→ Auto-scaling lanza nuevo Server 1'
→ Downtime: < 30 segundos
```

#### 3. Implementación Más Rápida y con Menos Riesgos

**Ventajas:**
- ✅ Se comienza a trabajar más rápido
- ✅ No es necesaria una gran inversión inicial (CAPEX)
- ✅ Reducción de riesgo de inversión en hardware

**Comparativa:**
```
Datacenter Tradicional:
1. Aprobar presupuesto: 2 meses
2. Comprar hardware: 1 mes
3. Instalar y configurar: 1 mes
4. Testing: 2 semanas
TOTAL: ~4.5 meses

Cloud:
1. Crear cuenta: 10 minutos
2. Provisionar recursos: 5 minutos  
3. Desplegar aplicación: 30 minutos
TOTAL: ~45 minutos

Velocidad: 99.5% más rápido
```

#### 4. Escalamiento Dinámico (Elastic Scaling)

**Ventaja:** Permite scaling out y scaling in de acuerdo a los requerimientos cambiantes de las aplicaciones.

**Tipos:**
- **Scaling Out (Horizontal):** Añadir más instancias
- **Scaling Back (Horizontal):** Reducir instancias
- **Scaling Up (Vertical):** Aumentar capacidad instancia
- **Scaling Down (Vertical):** Reducir capacidad instancia

```python
# Auto-scaling elástico en AWS
import boto3

autoscaling = boto3.client('autoscaling')

# Configurar escalado automático
autoscaling.put_scaling_policy(
    AutoScalingGroupName='mi-aplicacion',
    PolicyName='scale-dynamically',
    PolicyType='TargetTrackingScaling',
    TargetTrackingConfiguration={
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'ASGAverageCPUUtilization'
        },
        'TargetValue': 70.0  # Mantener CPU en 70%
    }
)

# Resultado:
# - Tráfico bajo: 2 instancias (ahorro)
# - Tráfico medio: 5 instancias (óptimo)
# - Pico tráfico: 20 instancias (soporta carga)
# - Automático, sin intervención manual
```

#### 5. Actualizaciones Automáticas

**Ventajas:**
- ✅ No afectan negativamente a los recursos de TIC
- ✅ Ahorro de tiempo y recursos para personalizar e integrar actualizaciones
- ✅ Siempre última versión de servicios
- ✅ Patches de seguridad aplicados automáticamente

**Ejemplo SaaS:**
- Salesforce: Actualización 3 veces/año, transparente
- Office 365: Actualizaciones continuas
- Sin downtime, sin esfuerzo del usuario

#### 6. Alta Disponibilidad y Durabilidad

**Ventaja:** El cloud ofrece:
- ✅ Plataforma para aplicaciones con acceso y almacenamiento confiable
- ✅ Alta disponibilidad de los recursos computacionales
- ✅ SLAs típicos: 99.9% - 99.99% uptime

**Ejemplo Amazon S3:**
- Durabilidad: 99.999999999% (11 noves)
- Disponibilidad: 99.99%
- Replicación automática en 3 zonas

```python
# Alta disponibilidad configurada automáticamente
s3 = boto3.client('s3')

s3.create_bucket(
    Bucket='mi-aplicacion-datos',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1'
    }
)

# AWS automáticamente:
# - Replica datos en 3 datacenters separados
# - Monitorea integridad continuamente
# - Repara automáticamente si detecta corrupción
# - Garantiza disponibilidad 99.99%
```

#### 7. Contribuye al Uso Eficiente de la Energía

**Ventaja:** Las organizaciones no requieren mantener datacenters que consumen gran energía.

**Eficiencia energética:**
```
Datacenter tradicional empresa:
- PUE (Power Usage Effectiveness): 2.0
- Por cada 1W en servidores, 2W totales (1W cooling/infraestructura)
- Utilización típica: 20-30%

Datacenter AWS/Google/Azure:
- PUE: 1.2
- Utilización: 70-80% (multi-tenancy)
- Energías renovables: 50-100%

Ahorro energético: ~75% por workload
```

### Desventajas y Limitaciones

#### 1. Centralización y Dependencia del Proveedor

**Problema:** La centralización de aplicaciones y almacenamiento origina interdependencia de los proveedores de servicios.

❌ **Vendor Lock-in:** Difícil migrar a otro proveedor
❌ **Dependencia total:** Si el proveedor quiebra, problema grave
❌ **Cambios de precios:** Provider puede subir precios

**Mitigación:**
```python
# Usar abstracciones para reducir lock-in
# En lugar de APIs propietarias, usar estándares

# ❌ MAL: Específico de AWS
import boto3
s3 = boto3.client('s3')
s3.put_object(Bucket='mybucket', Key='file.txt', Body=data)

# ✅ MEJOR: Abstracción con Apache Libcloud
from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver

cls = get_driver(Provider.S3)  # Cambiar fácilmente a GCS u otro
driver = cls('api_key', 'api_secret')
container = driver.get_container(container_name='mybucket')
container.upload_object('file.txt', object_name='file.txt')

# Ahora puedes cambiar Provider.S3 por Provider.GOOGLE_STORAGE
# Sin cambiar resto del código
```

#### 2. Disponibilidad Sujeta a Internet

**Problema:** La disponibilidad de los servicios está sujeta a la disponibilidad de acceso a Internet.

❌ **Sin Internet = Sin servicio**
❌ **Latencia de red** puede afectar performance
❌ **Costes de ancho de banda** al transferir datos

**Casos problemáticos:**
- Zonas rurales con conectividad pobre
- Aplicaciones de ultra-baja latencia (<1ms)
- Transferencias masivas de datos (100s de TB)

**Solución: Arquitectura híbrida/edge computing**

#### 3. Vulnerabilidad de Datos Sensibles

**Problema:** Los datos "sensibles" del negocio no residen en las instalaciones de las empresas, lo que podría generar un contexto de vulnerabilidad.

 ❌ **Privacidad:** Terceros tienen acceso físico a servidores
❌ **Compliance:** Puede no cumplir regulaciones (HIPAA, GDPR)
❌ **Soberanía de datos:** Datos pueden estar en otro país

**Mitigación:**
```python
# Encriptación end-to-end
import boto3
from cryptography.fernet import Fernet

# 1. Encriptar ANTES de subir a cloud
key = Fernet.generate_key()
cipher = Fernet(key)

data_sensible = "Datos médicos del paciente..."
data_encriptada = cipher.encrypt(data_sensible.encode())

# 2. Subir datos encriptados
s3 = boto3.client('s3')
s3.put_object(
    Bucket='datos-sensibles',
    Key='paciente_12345_encrypted.bin',
    Body=data_encriptada,
    ServerSideEncryption='AES256'  # Doble encriptación
)

# 3. Solo tú tienes la clave de desencriptación
# Ni AWS puede leer los datos
```

#### 4. Confiabilidad Dependiente del Proveedor

**Problema:** La confiabilidad de los servicios depende de la "salud" tecnológica y financiera de los proveedores.

❌ **Outages:** Fallos del proveedor afectan a miles de clientes
❌ **SLA** no siempre cumplido al 100%
❌ **Compensación limitada:** Créditos, no compensación real de pérdidas

**Ejemplo de outages famosos:**
- AWS US-East-1 outage (2017): Afectó a miles de sitios
- Google Cloud outage (2019): YouTube, Snapchat caídos
- Azure outage (2020): Microsoft Teams inaccesible

**Mitigación: Multi-cloud o multi-región**

#### 5. Escalabilidad a Largo Plazo (Riesgo de Sobrecarga)

**Problema:** A medida que más usuarios comparten la infraestructura de la nube, la sobrecarga en los servidores de los proveedores aumentará.

❌ Si el proveedor no dispone de un esquema de crecimiento óptimo puede llevar a:
- Degradaciones en el servicio
- Altos niveles de jitter (variabilidad de latencia)
- Rendimiento impredecible

**Realidad:** Los grandes proveedores (AWS, Azure, GCP) invierten billones en infraestructura, este problema es mínimo.

#### 6. Complejidad de los Servicios Cloud

**Problema:** Los servicios del cloud son más complejos que los servicios tradicionales.

❌ **Curva de aprendizaje:** Cientos de servicios, cada uno con configuraciones
❌ **Configuración incorrecta:** Puede llevar a brechas de seguridad
❌ **Costes inesperados:** Fácil gastar más de lo planeado

**Ejemplo de complejidad:**
AWS tiene 200+ servicios:
- EC2, S3, RDS, Lambda, DynamoDB, Kinesis, Redshift, EMR, SageMaker, ECS, EKS, CloudFormation, CloudWatch, IAM, VPC, Route 53, CloudFront, SNS, SQS, Step Functions...

Aprender todos: Años de experiencia

#### 7. Privacidad de la Información

**Problema:** La información queda expuesta a terceros.

❌ **Acceso del proveedor:** Empleados del proveedor pueden tener acceso
❌ **Subpoenas legales:** Gobiernos pueden solicitar datos
❌ **Ubicación física:** Datos pueden estar en jurisdicción que no controlas

#### 8. Seguridad de la Información

**Problema:** La información debe recorrer nodos para llegar a su destino, cada uno (y sus canales) son un foco de inseguridad.

❌ **Man-in-the-middle attacks**
❌ **Protocolos seguros (HTTPS)** disminuyen velocidad (overhead)
❌ **Responsabilidad compartida:** Proveedor y cliente comparten responsabilidad

**Modelo de responsabilidad compartida (AWS):**
```
┌──────────────────────────────────────┐
│  CLIENTE RESPONSABLE DE:             │
│  - Datos                             │
│  - Configuración SO                  │
│  - Aplicaciones                      │
│  - IAM (accesos)                     │
│  - Encriptación client-side          │
│  - Configuración Firewall            │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│  AWS RESPONSABLE DE:                 │
│  - Hardware / Infraestructura física │
│  - Virtualización                    │
│  - Seguridad física datacenters      │
│  - Redes globales                    │
│  - Regiones / Zonas disponibilidad   │
└──────────────────────────────────────┘
```

❗ **Importante:** La mayoría de brechas en cloud son por **mala configuración del cliente**, no fallos del proveedor.

#### 9. Manejo de Estándares Aún Inmaduro

**Problema:** El manejo de estándares para el despliegue de nubes aún no está del todo establecido.

❌ **Falta de estandarización** entre proveedores
❌ **APIs propietarias** diferentes
❌ **Portabilidad limitada** entre clouds

**Estandarización en proceso:**
- **Cloud Standards**: https://cloud-standards.org/
- **TOSCA** (Topology and Orchestration Specification for Cloud Applications)
- **OCCI** (Open Cloud Computing Interface)
- **CIMI** (Cloud Infrastructure Management Interface)

Pero aún lejos de ser universal.

#### 10. Requiere Buenas Prácticas

**Problema:** Se requieren fuertes fundamentos de "buenas prácticas" en:
- Desarrollo de software
- Arquitectura de software
- Gestión de servicios

❌ Sin buenas prácticas:
- Arquitecturas monolíticas que no escalan
- Aplicaciones stateful que no toleran fallas
- Seguridad débil (credenciales hardcodeadas)
- Costes descontrolados

**Solución: Adoptar metodologías como:**
- 12-Factor App
- Microservicios
- DevOps / CI/CD
- Infrastructure as Code
- Observabilidad (logging, monitoring, tracing)

#### 11. Consumo Energético de Datacenters

**Paradoja:** Aunque el cloud puede ser más eficiente, los clouds están conformados por grandes datacenters que consumen gran energía en total.

**Realidad:**
- Datacenter de AWS/Google: 50-100 MW (potencia de ciudad pequeña)
- Refrigeración masiva necesaria
- Impacto ambiental significativo

**Contraargumento:**
Despite el consumo absoluto, el cloud es más eficiente que miles de pequeños datacenters empresariales.

Además, proveedores invierten en energías renovables:
- Google Cloud: 100% energía renovable (2017+)
- AWS: Objetivo 100% renovable para 2025
- Azure: 100% renovable para 2025

### Balance: ¿Cuándo Usar Cloud?

**SÍ usar cloud si:**
- ✅ Startup o PYME con poco CAPEX
- ✅ Carga de trabajo variable/impredecible
- ✅ Necesitas escalar rápido (time-to-market)
- ✅ Desarrollo y testing (entornos efímeros)
- ✅ Innovación y experimentación
- ✅ No tienes equipo IT especializado
- ✅ Cumplimiento legal permite datos en cloud

**NO usar cloud (o usar híbrido) si:**
- ❌ Datos extremadamente sensibles (defensa, inteligencia)
- ❌ Regulaciones prohíben datos fuera de instalaciones
- ❌ Carga de trabajo 100% constante y predecible a largo plazo
- ❌ Latencia ultra-baja crítica (<1ms)
- ❌ Transferencias masivas continuas de datos

## 3.5. Retos y Desafíos en Cloud Computing

### Visión General de Retos

La construcción y operación de clouds enfrenta múltiples desafíos técnicos y organizacionales:

```
┌───────────────────────────────────────────────────────┐
│           RETOS PRINCIPALES EN CLOUD                  │
│                                                       │
│  ┌──────────────┐    ┌──────────────┐               │
│  │ Virtualización│    │ Servicios Web│               │
│  │ - Rendimiento │    │ - APIs       │               │
│  │ - Control     │    │ - Estándares │               │
│  └──────────────┘    └──────────────┘               │
│                                                       │
│  ┌──────────────┐    ┌──────────────┐               │
│  │  Seguridad y │    │ Contabilidad │               │
│  │  Privacidad  │    │ - Medición   │               │
│  │              │    │ - Costes     │               │
│  └──────────────┘    └──────────────┘               │
│                                                       │
│            ┌──────────────────┐                      │
│            │ Calidad Servicio │                      │
│            │ (QoS)            │                      │
│            └──────────────────┘                      │
└───────────────────────────────────────────────────────┘
```

### Reto 1: Calidad de Servicio (QoS)

**Problema:** La ausencia de QoS puede generar que las organizaciones declinen del uso del cloud.

**Aspectos críticos:**

1. **Ancho de Banda Suficiente**
   - El compartimiento de recursos y datos complejos requiere suficiente ancho de banda sin generar más costos
   - Transferencia de grandes volúmenes de datos (TBs) puede ser costosa y lenta

2. **Operaciones Libres de Fallas**
   - Debe ofrecer operaciones libres de fallas
   - Realidad: Un cloud puede experimentar fallas regulares
   - Necesidad de mecanismos de tolerancia a fallos

**Desafíos QoS:**

| Aspecto | Desafío | Solución |\n|---------|---------|----------|\n| **Latencia** | Variable según carga | Multi-región, edge computing |\n| **Throughput** | Compartido entre tenants | QoS policies, reserva de recursos |\n| **Disponibilidad** | SLA 99.9% = 8.76h downtime/año | Multi-AZ, auto-failover |\n| **Jitter** | Variabilidad impredecible | Networking dedicado, Direct Connect |

**Ejemplo: SLA de AWS EC2**
```
AWS EC2 SLA:
- Single AZ: 99.5% uptime
- Multi-AZ (misma región): 99.99% uptime
- Multi-Región: 99.999% uptime (teórico)

99.99% uptime = 52.56 minutos downtime/año
99.5% uptime = 1.83 días downtime/año

Diferencia: Multi-AZ es 20x más confiable
```

### Reto 2: Seguridad y Privacidad

**Problema:** De primordial importancia,dado que los datos se comparten en el cloud y están susceptibles a ataques cibernéticos.

**Vectores de Amenaza:**

1. **Ataques externos:**
   - DDoS (Distributed Denial of Service)
   - Inyección SQL
   - Cross-Site Scripting (XSS)
   - Man-in-the-Middle

2. **Amenazas internas:**
   - Empleados maliciosos del proveedor
   - Configuración incorrecta (más común)
   - Credenciales comprometidas

3. **Multi-tenancy:**
   - Aislamiento entre clientes
   - Side-channel attacks
   - Resource exhaustion

### Reto 3: Virtual ización

**Problema:** Los accesos simultáneos de múltiples clientes a los servicios del cloud demandan más protección y control.

**Desafíos:**

1. **Rendimiento**
   - Overhead de virtualización (5-10%)
   - "Noisy neighbor" problem: Un tenant consume recursos excesivos, afecta a otros

2. **Control de Recursos**
   - Optimizar desempeño de aplicaciones
   - Mejorar utilización de recursos
   - Reducir consumo de energía

3. **Aislamiento**
   - Garantizar que tenants no puedan acceder a datos de otros
   - VM escape attacks

### Reto 4: Servicios Web y APIs

**Problema:** Ofrecer interfaces sencillas que escondan la heterogeneidad de hardware y software en el cloud.

**Desafíos:**

1. **Estandarización de APIs**
   - Cada proveedor tiene APIs propietarias
   - Falta de estándar universal
   - Dificulta portabilidad

2. **Complejidad**
   - AWS tiene 200+ servicios, cada uno con su API
   - Azure similar
   - Curva de aprendizaje alta

### Reto 5: Contabilidad y Control de Costes

**Problema:** Se requiere control de costos para no desbordar a las organizaciones con incrementos de pagos.

**Desafíos:**

1. **Complejidad de Pricing**
   - Cientos de dimensiones de coste
   - Diferentes precios por región
   - Descuentos por volumen, reservas
   - Difícil estimar costes futuros

2. **Costes inesperados**
   - Recursos olvidados ("zombie resources")  
   - Snapshots acumulados
   - Logs no rotados
   - Auto-scaling mal configurado

## 3.6. Estrategias de Adopción de Cloud Computing

### Ciclo de Vida de Adopción

```
┌──────────────────────────────────────────────────────┐
│      CICLO DE VIDA DE ADOPCIÓN DE CLOUD             │
│                                                      │
│  Fase 1: EVALUACIÓN (Assessment)                    │
│       ↓                                              │
│  Fase 2: PRUEBA DE CONCEPTO (PoC)                   │
│       ↓                                              │
│  Fase 3: MIGRACIÓN PILOTO                           │
│       ↓                                              │
│  Fase 4: PRUEBAS                                     │
│       ↓                                              │
│  Fase 5: GO-LIVE (Producción)                       │
│       ↓                                              │
│  Fase 6: AUDITORÍA Y OPTIMIZACIÓN                   │
└──────────────────────────────────────────────────────┘
```

### Cuatro Estrategias Principales de Adopción

#### 1. Scalability-Driven Strategy (Orientada a la Escalabilidad)

**Definición:** Uso de los recursos del cloud para soportar cargas adicionales o como respaldo.

**Casos de uso:**
- **Cloud Bursting:** Workload normal en on-premise, picos en cloud
- **Auto-scaling horizontal:** Añadir instancias automáticamente

**Ejemplo:**
```
E-commerce durante Black Friday:
- Capacidad base (on-premise): 10,000 req/sec
- Pico Black Friday: 100,000 req/sec
- Burst a cloud: +90,000 req/sec adicionales
- Solo durante el evento (1 día)
```

#### 2. Availability-Driven Strategy (Orientada a la Disponibilidad)

**Definición:** Uso de recursos del cloud balanceados y localizados para incrementar la disponibilidad y reducir los tiempos de respuesta.

**Casos de uso:**
- **Multi-región deployment:** Aplicación en múltiples regiones geográficas
- **Disaster Recovery:** Cloud como backup de datacenter principal
- **Edge locations:** Content Delivery Networks (CDNs)

#### 3. Market-Driven Strategy (Orient ada al Negocio)

**Definición:** Usuarios y proveedores de los recursos del cloud toman decisiones basadas en el potencial ahorro y ganancias.

**Enfoque:** Puramente económico/financiero

**Casos de uso:**
- **Startups:** Evitar CAPEX masivo, usar OPEX
- **Empresas en crecimiento:** Escalar según demanda
- **Proyectos temporales:** Solo pagar durante el proyecto

#### 4. Convenience-Driven Strategy (Orientada a la Conveniencia)

**Definición:** Uso de los recursos del cloud para no mantener recursos locales.

**Motivación:** Simplicidad operativa

**Casos de uso:**
- **Empresas sin equipo IT:** No tienen capacidad de gestionar datacenter
- **Focus en core business:** Empresa de salud quiere centrarse en medicina, no en IT
- **Eliminar complejidad:** No gestionar hardware, actualizaciones, seguridad física

### Selección de Estrategia: Factores Clave

Para elegir la estrategia apropiada de adopción, considerar:

**Preguntas estratégicas:**

1. **¿Dónde aportará valor al negocio actual?**
   - Reducción de costes
   - Mejora de agilidad
   - Nuevas capacidades (ML, analytics)
   - Mejor experiencia de usuario

2. **¿Puede ser implementado solo en áreas seleccionadas del negocio?**
   - Comenzar con workloads no críticos
   - Enfoque híbrido: Crítico on-premise, resto cloud

3. **¿Cuánto se puede controlar de la migración?**
   - Migración gradual (meses/años)
   - Big bang (todo de una vez) - ⚠️ Alto riesgo

**Las respuestas a estas preguntas deben conducir a las decisiones de la organización de implementar el cloud sobre la base de:**
- ✅ Escalabilidad
- ✅ Disponibilidad
- ✅ Coste
- ✅ Conveniencia
