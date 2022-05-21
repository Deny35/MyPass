    def selectItem(self, event):
                curItem = self.tree.item(self.tree.focus())
                col = self.tree.identify_column(event.x)
                id = curItem['values'][0]

                if col == '#1':
                    pass
                elif col == '#2':
                    what = 'name'
                    name = curItem['values'][1]
                elif col == '#3':
                    what = 'login'
                    name = curItem['values'][2]
                elif col == '#4':
                    what = 'password'
                    name = curItem['values'][3]