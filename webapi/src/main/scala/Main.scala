import akka.actor.ActorSystem
import akka.http.scaladsl.Http
import akka.http.scaladsl.server.Directives._
import akka.stream.ActorMaterializer
import spray.json.DefaultJsonProtocol
import akka.http.scaladsl.marshallers.sprayjson.SprayJsonSupport
import scala.io.StdIn

case class PetFace(eye_left_x: Float, eye_left_y: Float, eye_right_x: Float, eye_right_y: Float,
                   nose_x: Float, nose_y: Float, mouth_x: Float, mouth_y: Float, score: Float)

trait JsonSupport extends SprayJsonSupport with DefaultJsonProtocol {
  implicit val petFaceFormat = jsonFormat9(PetFace.apply)
}

object Main extends JsonSupport {
  def main(args: Array[String]) = {
    implicit val system = ActorSystem("my-system")
    implicit val materializer = ActorMaterializer()
    implicit val executionContext = system.dispatcher

    val route =
      path("pet") {
        get {
          val v = PetFace(0,0,0,0,0,0,0,0,0)
          complete(
            Seq(v, v, v, v, v)
          )
        }
      } ~
      path("pet") {
        post {
          entity(as[Seq[PetFace]]) { request =>
            complete("POST hoge")
          }
        }
      }


    val bindingFuture = Http().bindAndHandle(route, "localhost", 8080)

    println(s"Server online at http://localhost:8080/\nPress RETURN to stop...")
    StdIn.readLine() // let it run until user presses return
    bindingFuture
      .flatMap(_.unbind()) // trigger unbinding from the port
      .onComplete(_ => system.terminate()) // and shutdown when done
  }
}
