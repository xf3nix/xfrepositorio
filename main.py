import kivy
kivy.require('1.11.1')
from kivy.config import Config
Config.set('graphics', 'width', 340)
Config.set('graphics', 'height', 640)
Config.set('graphics', 'resizable', True)
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from BD.mysqli import consultatodo, consultasector
from kivy.uix.screenmanager import Screen
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.properties import ObjectProperty, StringProperty


def populate_tree_view(tree_view, parent, node):

    if parent is None:
        tree_node = tree_view.add_node(TreeViewLabel(text=node['node_id'],
                                                     is_open=True))
    else:
        tree_node = tree_view.add_node(TreeViewLabel(text=node['node_id'],
                                                     is_open=True), parent)
    for child_node in node['children']:
        populate_tree_view(tree_view, tree_node, child_node)


# Funciones telefono y consulta productos
class TreeViewGroup(Popup):

    tree_view = ObjectProperty(None)
    tv = ObjectProperty(None)
    ti = ObjectProperty(None)
    filter_text = StringProperty('')

    def __init__(self, **kwargs):
        super(TreeViewGroup, self).__init__(**kwargs)

        ver = self.cimagentodo()
        self.rows = []

        for y in ver.values():
            self.rows.append(y)

    def on_open(self, *args):
        self.obj = self.ti
        self.ti.focus = True
        self.filter_text = MDApp.get_running_app().root.name.text

    def create_tree_view_root(self):
        self.tv = TreeView(root_options=dict(text=""),
                           hide_root=True,
                           indent_level=4)

    def create_tree_view_branch(self, obj):
        for branch in obj:
            populate_tree_view(self.tv, None, branch)
        self.tree_view.add_widget(self.tv)

    def dismiss_callback(self):
        self.dismiss()

    def filter(self, value):

        self.rw = []
        for i in self.rows:
            if str(i[0]) == value[0:2].strip():
                self.rw.append(i)

        self.tree_view.clear_widgets()
        self.create_tree_view_root()

        self.tre = [{'node_id': str(p[1]).strip(), 'children': []} for p in self.rw]

        print(self.tre)
        self.create_tree_view_branch(self.tre)

    def cimagentodo(self):
        image = consultatodo()
        paquetes = {}
        r = ""
        try:
            for row in image:
                if r != row[0]:
                    paquetes.setdefault(row[0], (row[1], row[2]))
                else:
                    paquetes[row[0]] = (row[1], row[2])
                r = row[0]

            return paquetes
        except:
            pass


# Carga y pdf
class GroupScreen(Screen):

    name = ObjectProperty(None)
    popup = ObjectProperty(None)

    lista = []
    valor = ""
    texto = ""

    def __init__(self, **kwargs):
        super(GroupScreen, self).__init__(**kwargs)

        clients = self.consultasector()

        bridge_view = TreeView()        
        for s in clients:
            x = str(s[0]) + " - " + str(s[1])
            bridge_view.add_node(TreeViewLabel(text=str(x).capitalize(),
                                               even_color=[0.5,0.1,0.1,1],
                                               odd_color=[0.1,0.1,0.5,1]))

        self.add_widget(bridge_view)

    def display_groups(self, instance):

        if len(instance.text) > 0:
            if self.popup is None:
                self.popup = TreeViewGroup()
            self.popup.open()

    def cargar(self):

        if self.ids.name.text != "Presione para buscar":
            self.valor = str(self.ids.name.text)
            tex = ""
            self.lista.append(self.valor)
            for i in self.lista:
                tex = i
            self.texto += tex + "\n\n"
            self.ids.cust.text = str(self.texto).lower()
            self.ids.name.text = "Presione para buscar"
            self.ids.pdf.disabled = False

    def borrar(self):
        self.valor = ""
        self.texto = ""
        self.lista.clear()
        self.ids.name.text = "Presione para buscar"
        self.ids.cust.text = ""
        self.ids.pdf.disabled = False

    def exit(self):
        MDApp.get_running_app().stop()

    def consultasector(self):

        image = consultasector()
        paquetes = []

        try:
            for row in image:
                paquetes.append(row)
            return paquetes
        except:
            pass


class Group(MDApp):
    def build(self):
        self.root = Builder.load_file('test.kv')
        return self.root


if __name__ == '__main__':
    Group().run()
