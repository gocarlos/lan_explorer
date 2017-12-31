#include <fstream>
#include <iostream>
#include <string>

#include <gtkmm.h>

#include "lan-explorer/settings.hpp"


//Gtk::Dialog* pDialog = nullptr;

Gtk::Window* pDialog = nullptr;

static
void on_button_clicked()
{
  if(pDialog)
    pDialog->hide(); //hide() will cause main::run() to end.
}

int main(int argc, char *argv[]) {
  std::cout << "Hello world\n";

  const std::string home_path = lan_explorer_settings::root_directory;

  std::cout << home_path << std::endl;
  auto app = Gtk::Application::create(argc, argv, "ch.martinho.lan_explorer");

  // Load the GtkBuilder file and instantiate its widgets:
  auto refBuilder = Gtk::Builder::create();
  try {
    std::string layout =  home_path + "rsc/main_view.glade";
    std::cout << layout << std::endl;

    refBuilder->add_from_file(layout);
  } catch (const Glib::FileError &ex) {
    std::cerr << "FileError: " << ex.what() << std::endl;
    return 1;
  } catch (const Glib::MarkupError &ex) {
    std::cerr << "MarkupError: " << ex.what() << std::endl;
    return 1;
  } catch (const Gtk::BuilderError &ex) {
    std::cerr << "BuilderError: " << ex.what() << std::endl;
    return 1;
  }


  //Get the GtkBuilder-instantiated Dialog:
  refBuilder->get_widget("DialogBasic", pDialog);
  if(pDialog)
  {
    //Get the GtkBuilder-instantiated Button, and connect a signal handler:
    Gtk::Button* pButton = nullptr;
    refBuilder->get_widget("quit_button", pButton);
    if(pButton)
    {
      pButton->signal_clicked().connect( sigc::ptr_fun(on_button_clicked) );
    }

    app->run(*pDialog);
  }

  delete pDialog;

  // Gtk::Window window;
  // window.set_default_size(200, 200);

  // return app->run(window);

  return 0;
}
