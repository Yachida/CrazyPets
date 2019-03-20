scalaVersion := "2.11.8"

libraryDependencies ++= {
  Seq(
    "com.typesafe.akka" %% "akka-http" % "10.1.7",
    "com.typesafe.akka" %% "akka-stream" % "2.5.19",
    "com.typesafe.akka" %% "akka-http-spray-json" % "10.1.7",
    "io.spray" %%  "spray-json" % "1.3.5"
  )
}
